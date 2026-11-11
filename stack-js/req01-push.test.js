const { Stack } = require("./stack");

describe("Req 1: push", () => {
  test("pushes one item onto an empty stack", () => {
    const stack = new Stack();
    stack.push(1);
    expect(stack.toArray()).toEqual([1]);
  });

  test("each new item goes on top", () => {
    const stack = new Stack();
    stack.push(1);
    stack.push(2);
    stack.push(3);
    expect(stack.toArray()).toEqual([1, 2, 3]);
  });

  test("stores mixed data types unchanged", () => {
    const stack = new Stack();
    const arr = [4];
    const obj = { a: 1 };
    [1, "two", true, null, arr, obj].forEach((v) => stack.push(v));
    expect(stack.toArray()).toEqual([1, "two", true, null, arr, obj]);
  });

  test("allows duplicate values", () => {
    const stack = new Stack();
    stack.push(5);
    stack.push(5);
    expect(stack.toArray()).toEqual([5, 5]);
  });
});
