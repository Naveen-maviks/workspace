const { Stack } = require("./stack");

const make = (...items) => {
  const stack = new Stack();
  items.forEach((i) => stack.push(i));
  return stack;
};

describe("Req 5: isEmpty", () => {
  test("a new stack is empty", () => {
    expect(new Stack().isEmpty()).toBe(true);
  });

  test("a stack with one item is not empty", () => {
    expect(make(1).isEmpty()).toBe(false);
  });

  test("a stack holding falsy values is not empty", () => {
    expect(make(0).isEmpty()).toBe(false);
    expect(make(null).isEmpty()).toBe(false);
    expect(make("").isEmpty()).toBe(false);
  });

  test("becomes not empty after a push", () => {
    const stack = new Stack();
    stack.push(1);
    expect(stack.isEmpty()).toBe(false);
  });

  test("becomes empty after popping every item", () => {
    const stack = make(1, 2);
    stack.pop();
    expect(stack.isEmpty()).toBe(false);
    stack.pop();
    expect(stack.isEmpty()).toBe(true);
  });

  test("peek does not make the stack empty", () => {
    const stack = make(1);
    stack.peek();
    expect(stack.isEmpty()).toBe(false);
  });

  test("agrees with size", () => {
    const stack = make(1);
    expect(stack.isEmpty()).toBe(stack.size === 0);
    stack.pop();
    expect(stack.isEmpty()).toBe(stack.size === 0);
  });
});
