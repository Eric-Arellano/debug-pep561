python_library()
resources(name="py.typed", sources=["py.typed"])
python_distribution(
  name="dist",
  dependencies=[":mypkg", ":py.typed"],
  provides=setup_py(name="dist", version="0.1.0"),
  setup_py_commands=["bdist_wheel"],
)
