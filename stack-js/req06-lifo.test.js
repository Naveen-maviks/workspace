const { Stack } = require("./stack");

const make = (...items) => {
  const stack = new Stack();
  items.forEach((i) => stack.push(i));
  return stack;
};

describe("Req 6: LIFO order", () => {
  test("the last item pushed is the first item popped", () => {
    const stack = make(1, 2, 3);
    expect(stack.pop()).toBe(3);
  });

  test("items come out in the reverse of the order they went in", () => {
    const stack = make("a", "b", "c", "d");
    const out = [];
    while (!stack.isEmpty()) out.push(stack.pop());
    expect(out).toEqual(["d", "c", "b", "a"]);
  });

  test("the top is always the most recent push", () => {
    const stack = new Stack();
    stack.push(1);
    expect(stack.peek()).toBe(1);
    stack.push(2);
    expect(stack.peek()).toBe(2);
    stack.push(3);
    expect(stack.peek()).toBe(3);
  });

  test("pushing after a pop puts the new item on top", () => {
    const stack = make(1, 2, 3);
    stack.pop();
    stack.push(9);
    expect(stack.pop()).toBe(9);
    expect(stack.pop()).toBe(2);
  });

  test("order is kept for mixed types", () => {
    const obj = { a: 1 };
    const stack = make(1, "two", null, obj);
    expect(stack.pop()).toBe(obj);
    expect(stack.pop()).toBeNull();
    expect(stack.pop()).toBe("two");
    expect(stack.pop()).toBe(1);
  });

  test("duplicates keep their place in the order", () => {
    const stack = make(5, 7, 5);
    expect(stack.pop()).toBe(5);
    expect(stack.pop()).toBe(7);
    expect(stack.pop()).toBe(5);
  });

  test("reversing a string with a stack", () => {
    const stack = new Stack();
    for (const ch of "hello") stack.push(ch);
    let reversed = "";
    while (!stack.isEmpty()) reversed += stack.pop();
    expect(reversed).toBe("olleh");
  });
});
