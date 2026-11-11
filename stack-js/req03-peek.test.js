const { Stack } = require("./stack");

const make = (...items) => {
  const stack = new Stack();
  items.forEach((i) => stack.push(i));
  return stack;
};

describe("Req 3: peek", () => {
  test("returns the top item", () => {
    expect(make(1, 2, 3).peek()).toBe(3);
  });

  test("does not remove the top item", () => {
    const stack = make(1, 2, 3);
    stack.peek();
    expect(stack.toArray()).toEqual([1, 2, 3]);
  });

  test("peeking twice gives the same item", () => {
    const stack = make("a", "b");
    expect(stack.peek()).toBe("b");
    expect(stack.peek()).toBe("b");
  });

  test("works on a stack with one item", () => {
    expect(make(7).peek()).toBe(7);
  });

  test("returns items of any type unchanged", () => {
    const obj = { a: 1 };
    expect(make(1, obj).peek()).toBe(obj);
    expect(make(1, null).peek()).toBeNull();
  });

  test("shows the new top after a pop", () => {
    const stack = make(1, 2, 3);
    stack.pop();
    expect(stack.peek()).toBe(2);
  });

  test("peeking an empty stack throws an error", () => {
    expect(() => new Stack().peek()).toThrow("stack is empty");
  });
});
