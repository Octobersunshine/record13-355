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


def custom_sum(expr: str, n: int, start: int = 1) -> float:
    import math

    if not isinstance(expr, str) or not expr.strip():
        raise ValueError("通项公式 expr 必须为非空字符串")
    if n <= 0:
        raise ValueError("项数 n 必须为正整数")

    safe_globals = {
        "__builtins__": None,
        "abs": abs,
        "min": min,
        "max": max,
        "pow": pow,
        "round": round,
        "int": int,
        "float": float,
    }
    for name in dir(math):
        if not name.startswith("_"):
            safe_globals[name] = getattr(math, name)

    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+-*/()., %<>!&|~^")
    for ch in expr:
        if ch not in allowed_chars:
            raise ValueError(f"通项公式中包含非法字符: '{ch}'")

    total = 0.0
    code = compile(expr, "<user_expr>", "eval")
    for k in range(start, start + n):
        safe_locals = {"n": k}
        total += eval(code, safe_globals, safe_locals)
    return total


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

    print("\n=== 自定义通项公式求和 ===")
    print(f"Σ 2n-1 (n=1..5): {custom_sum('2*n - 1', 5)}")
    print(f"Σ n² (n=1..5): {custom_sum('n ** 2', 5)}")
    print(f"Σ 1/n (n=1..10, 调和部分和): {custom_sum('1 / n', 10)}")
    print(f"Σ sin(n*π/2) (n=1..4): {custom_sum('sin(n * pi / 2)', 4)}")
    print(f"Σ sqrt(n) (n=1..5): {custom_sum('sqrt(n)', 5)}")
