#!/usr/bin/env python3
"""Asyncio basics"""

import asyncio
import random
from typing import list

from .0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """concurrent coroutines"""
    array = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(queue):
        result = await task
        array.append(result)

    return array
