#!/usr/bin/env python3
"""Async basics"""

import asyncio
import random
import time


async  def wait_random(max_delay: int:10) -> float:
    """
    Defination of wait_random that waits for
    a random delay between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
