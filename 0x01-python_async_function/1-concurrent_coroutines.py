#!/usr/bin/env python3
"""Asyncio basics"""

import asyncio
import random
from typing import list

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """concurrent coroutines"""
    task, array = [], []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        result = await task
        array.append(result)

    return array
