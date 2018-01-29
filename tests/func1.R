describe("func1", {

  it("can be called with no arguments", {
    expect_equal(func1(), "Hello world!")
  })

  it("can be called with one argument", {
    expect_equal(func1("from R"), "Hello from R!")
  })

})
