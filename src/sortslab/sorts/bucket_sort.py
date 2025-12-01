from src.sortslab.sorts.insertion_sort import insertion_sort

def bucket_sort(arr: list[int], buckets_count: int | None = None) -> list[int]:
    if len(arr) <= 1:
        return arr
    if buckets_count is None:
        buckets_count = len(arr)
    min_num = min(arr)
    max_num = max(arr)
    buckets = [[] for _ in range(buckets_count)]
    buckets_range = (max_num - min_num) / buckets_count
    sorted_array =[]

    for num in arr:
        bucket_index = int((num - min_num) / buckets_range)
        if bucket_index == buckets_count:
            bucket_index -= 1
        buckets[bucket_index].append(num)

    for bucket in buckets:
        insertion_sort(bucket)
        sorted_array.extend(bucket)

    return sorted_array