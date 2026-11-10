const { List } = require("./list");

const make = (...items) => {
  const list = new List();
  items.forEach((i) => list.add(i));
  return list;
};

describe("Req 4: mutable", () => {
  test("changes a value in place", () => {
    const list = make(1, 2, 3);
    list.set(1, 99);
    expect(list.toArray()).toEqual([1, 99, 3]);
  });

  test("changes the first and last values", () => {
    const list = make(1, 2, 3);
    list.set(0, "a");
    list.set(2, "c");
    expect(list.toArray()).toEqual(["a", 2, "c"]);
  });

  test("can replace a value with a different type", () => {
    const list = make(1, 2);
    list.set(0, { a: 1 });
    expect(list.toArray()).toEqual([{ a: 1 }, 2]);
  });

  test("size does not change after set", () => {
    const list = make(1, 2, 3);
    list.set(1, 99);
    expect(list.toArray()).toHaveLength(3);
  });

  test("invalid index throws and leaves the list unchanged", () => {
    const list = make(1);
    expect(() => list.set(3, 5)).toThrow(RangeError);
    expect(() => list.set(-1, 5)).toThrow(RangeError);
    expect(list.toArray()).toEqual([1]);
  });

  test("setting on an empty list throws", () => {
    expect(() => new List().set(0, 1)).toThrow(RangeError);
  });
});
