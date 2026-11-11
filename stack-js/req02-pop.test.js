const { Stack } = require("./stack");

const make = (...items) => {
  const stack = new Stack();
  items.forEach((i) => stack.push(i));
  return stack;
};

describe("Req 2: pop", () => {
  test("returns the top item", () => {
    expect(make(1, 2, 3).pop()).toBe(3);
  });

  test("removes the top item from the stack", () => {
    const stack = make(1, 2, 3);
    stack.pop();
    expect(stack.toArray()).toEqual([1, 2]);
  });

  test("pops items in reverse order", () => {
    const stack = make("a", "b", "c");
    expect(stack.pop()).toBe("c");
    expect(stack.pop()).toBe("b");
    expect(stack.pop()).toBe("a");
  });

  test("can pop the only item, leaving an empty stack", () => {
    const stack = make(1);
    expect(stack.pop()).toBe(1);
    expect(stack.toArray()).toEqual([]);
  });

  test("returns items of any type unchanged", () => {
    const obj = { a: 1 };
    const stack = make(null, obj);
    expect(stack.pop()).toBe(obj);
    expect(stack.pop()).toBeNull();
  });

  test("popping an empty stack throws an error", () => {
    expect(() => new Stack().pop()).toThrow("stack is empty");
  });

  test("popping again after emptying the stack throws", () => {
    const stack = make(1);
    stack.pop();
    expect(() => stack.pop()).toThrow("stack is empty");
  });
});
