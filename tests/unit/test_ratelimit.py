from uex.core.ratelimit import TokenBucket


def test_bucket_allows_burst_up_to_rate() -> None:
    clock = [0.0]
    bucket = TokenBucket(3, 60.0, clock=lambda: clock[0])
    assert bucket.acquire_delay() == 0.0
    assert bucket.acquire_delay() == 0.0
    assert bucket.acquire_delay() == 0.0
    assert bucket.acquire_delay() > 0.0


def test_bucket_refills_over_time() -> None:
    clock = [0.0]
    bucket = TokenBucket(1, 60.0, clock=lambda: clock[0])
    bucket.acquire_delay()
    clock[0] = 60.0
    assert bucket.acquire_delay() == 0.0
