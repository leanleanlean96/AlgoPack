import typer
from src.sortslab.common import check_if_types_match
from src.sortslab.math_functions import factorial_dynamic
from src.sortslab.math_functions import factorial_recursive
from src.sortslab.math_functions import fibo_dynamic
from src.sortslab.math_functions import fibo_recursive
from src.sortslab.sorts import bubble_sort as bubble_sort_func
from src.sortslab.sorts import quick_sort as quick_sort_func
from src.sortslab.sorts import counting_sort as counting_sort_func
from src.sortslab.sorts import bucket_sort as bucket_sort_func
from src.sortslab.sorts import radix_sort as radix_sort_func
from src.sortslab.sorts import heap_sort as heap_sort_func
from src.sortslab.sorts import selection_sort as selection_sort_func
from src.sortslab.sorts import insertion_sort as insertion_sort_func
from typer_shell import make_typer_shell
from typing_extensions import Annotated






app = make_typer_shell()

@app.command()
def factorial(
            recursive: bool = typer.Option(
                False, "-r", "--recursive", help="Calculate the factorial function recursively"
            ),
            num: int = typer.Argument(...)
            ) -> None:
    if recursive:
        try:
            typer.echo(factorial_recursive(num))
        except RecursionError as e:
            typer.echo(e)
    else:
        try:
            typer.echo(factorial_dynamic(num))
        except Exception as e:
            typer.echo(e)

@app.command()
def fibonacci(
            recursive: bool = typer.Option(
                False, "-r", "--recursive", help="Calculate the factorial function recursively"
            ),
            num: int = typer.Argument(...)
            ) -> None:
    if recursive:
        try:
            typer.echo(fibo_recursive(num))
        except RecursionError as e:
            typer.echo(e)
    else:
        try:
            typer.echo(fibo_dynamic(num))
        except Exception as e:
            typer.echo(e)

@app.command()
def bubble_sort(
            arr: list[int] = typer.Argument(...)
            ) -> None:
    check_if_types_match("int", arr)
    sorted_arr = bubble_sort_func(arr)
    typer.echo(sorted_arr)

@app.command()
def quick_sort(
            arr: list[int] = typer.Argument(...)
            ) -> None:
    check_if_types_match("int", arr)
    typer.echo(quick_sort_func(arr))

@app.command()
def counting_sort(
            arr: list[int] = typer.Argument(...)
            ) -> None:
    check_if_types_match("int", arr)
    typer.echo(counting_sort_func(arr))

@app.command()
def radix_sort(
            arr: list[int] = typer.Argument(...),
            base: Annotated[int | None, typer.Argument()] = None
            ) -> None:
    check_if_types_match("int", arr)
    typer.echo(radix_sort_func(arr, base))

@app.command()
def bucket_sort(
            arr: list[float] = typer.Argument(...),
            buckets: Annotated[int | None, typer.Argument()] = None
            ) -> None:
    check_if_types_match("float", arr)
    typer.echo(bucket_sort_func(arr, buckets))

@app.command()
def heap_sort(
            arr: list[int] = typer.Argument(...)
            ) -> None:
    check_if_types_match("int", arr)
    typer.echo(heap_sort_func(arr))

@app.command()
def selection_sort(
            arr: list[int] = typer.Argument(...)
            ) -> None:
    check_if_types_match("int", arr)
    typer.echo(selection_sort_func(arr))

@app.command()
def insertion_sort(
            arr: list[int] = typer.Argument(...)
            ) -> None:
    check_if_types_match("int", arr)
    typer.echo(insertion_sort_func(arr))

if __name__ == "__main__":
    app()