from typing import List, Any, Callable, Coroutine
import asyncio


class ProductLoader:
    async def fetchProductInfo(self):
        # Simulate a long-running operation with asyncio.sleep
        await asyncio.sleep(5)  # Sleep for 10 seconds
        print("Product info fetched")
        return "Product info"
    

class ProductInfoFuture(asyncio.Future[Any]):
    def __init__(self, coroutine: Coroutine[Any, Any, Any]):
        super().__init__()
        asyncio.ensure_future(self._wrap_coroutine(coroutine))

    async def _wrap_coroutine(self, coroutine: Coroutine[Any, Any, Any]):
        result = await coroutine
        self.set_result(result)


class TestCase:
    def __init__(self, name: str, func: Callable[[], Coroutine[Any, Any, Any]] , dependencies: List[asyncio.Future[Any]]=[]):
        self.name = name
        self.func = func
        self.dependencies = dependencies if dependencies else []

    async def __call__(self):
        for dependency in self.dependencies:
            await dependency
        return await self.func()


class SampleProfile:
    def __init__(self, product_info: ProductInfoFuture):
        self.test_suite: List[TestCase] = []

        self.add_test_case('Test case 1', self.test_case_1)
        self.add_test_case('Test case 2', self.test_case_2, [product_info])
        self.add_test_case('Test case 3', self.test_case_3, [asyncio.ensure_future(self.test_suite[0]())])
    
    def add_test_case(self, name: str, func: Callable[[], Coroutine[Any, Any, Any]], dependencies: List[asyncio.Future[Any]]=[]):
        self.test_suite.append(TestCase(name, func, dependencies))


    async def test_case_1(self):
        await asyncio.sleep(1)  # simulate delay
        return 'Test case 1 passed'

    async def test_case_2(self):
        await asyncio.sleep(2)  # simulate delay
        return 'Test case 2 passed'

    async def test_case_3(self):
        await asyncio.sleep(3)  # simulate delay
        return 'Test case 3 passed'
    


    
async def main():
    product_loader = ProductLoader()
    fetch_product_info_future = ProductInfoFuture(product_loader.fetchProductInfo())
    profile = SampleProfile(fetch_product_info_future)

    # Separate tasks into independent and dependent tasks
    independent_tasks = [tc for tc in profile.test_suite if not tc.dependencies]
    dependent_tasks = [tc for tc in profile.test_suite if tc.dependencies]

    # Run independent tasks first
    for tc in independent_tasks:
        result = await tc()
        print(result)

    # Then run dependent tasks
    for tc in dependent_tasks:
        result = await tc()
        print(result)

asyncio.run(main())