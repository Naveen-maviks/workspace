const { Stack } = require("./stack");

const make = (...items) => {
  const stack = new Stack();
  items.forEach((i) => stack.push(i));
  return stack;
};

describe("Req 4: size", () => {
  test("an empty stack has size 0", () => {
    expect(new Stack().size).toBe(0);
  });

  test("size grows with every push", () => {
    const stack = new Stack();
    stack.push(1);
    expect(stack.size).toBe(1);
    stack.push(2);
    expect(stack.size).toBe(2);
  });

  test("duplicates are counted", () => {
    expect(make(5, 5, 5).size).toBe(3);
  });

  test("size goes down after a pop", () => {
    const stack = make(1, 2, 3);
    stack.pop();
    expect(stack.size).toBe(2);
  });

  test("size does not change after a peek", () => {
    const stack = make(1, 2, 3);
    stack.peek();
    expect(stack.size).toBe(3);
  });

  test("size is 0 after popping every item", () => {
    const stack = make(1, 2);
    stack.pop();
    stack.pop();
    expect(stack.size).toBe(0);
  });

  test("a failed pop does not change the size", () => {
    const stack = new Stack();
    expect(() => stack.pop()).toThrow("stack is empty");
    expect(stack.size).toBe(0);
  });
});
