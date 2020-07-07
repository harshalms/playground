def count_steps_pattern(n):
    count = 0
    if n<=3:
        return n
    return count_steps_pattern(n-1)+count_steps_pattern(n-2)

if __name__ == "__main__":
    print(count_steps_pattern(5))