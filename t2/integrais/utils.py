def print_value(x):
  print(f"{x:.8f}")


def print_values(x):
  for i, xi in enumerate(x):
    print(f"{xi:.8f}", end="")
    if (i != len(x) - 1):
      print(",", end="")
    else:
      print()