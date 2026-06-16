def arithmetic_sum(first: float, diff: float, n: int) -> float:
    if n <= 0:
        raise ValueError("项数 n 必须为正整数")
    return n * first + n * (n - 1) * diff / 2


def geometric_sum(first: float, ratio: float, n: int) -> float:
    if n <= 0:
        raise ValueError("项数 n 必须为正整数")
    if abs(ratio - 1) < 1e-12:
        return first * n
    return first * (1 - ratio ** n) / (1 - ratio)


def sum_of_squares(n: int) -> int:
    if n <= 0:
        raise ValueError("项数 n 必须为正整数")
    return n * (n + 1) * (2 * n + 1) // 6


def sum_of_cubes(n: int) -> int:
    if n <= 0:
        raise ValueError("项数 n 必须为正整数")
    return (n * (n + 1) // 2) ** 2


if __name__ == "__main__":
    print("=== 等差数列求和 ===")
    print(f"首项=1, 公差=2, 项数=5: {arithmetic_sum(1, 2, 5)}")

    print("\n=== 等比数列求和 ===")
    print(f"首项=1, 公比=2, 项数=5: {geometric_sum(1, 2, 5)}")
    print(f"首项=3, 公比=1, 项数=4: {geometric_sum(3, 1, 4)}")

    print("\n=== 平方和 ===")
    print(f"1²+2²+...+5² = {sum_of_squares(5)}")

    print("\n=== 立方和 ===")
    print(f"1³+2³+...+5³ = {sum_of_cubes(5)}")
