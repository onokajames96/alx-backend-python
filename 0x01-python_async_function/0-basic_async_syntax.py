#!/usr/bin/env python3

import asyncio
import random
import time

async  def wait_random(max_delay= int:10:) -> float:
    delay = random.uniform(0, max_delay)
    yield
    time.sleep(delay)
    await asyncio.sleep(delay)
    return delay
