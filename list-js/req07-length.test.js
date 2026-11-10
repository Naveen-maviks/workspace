const { List } = require("./list");

const make = (...items) => {
  const list = new List();
  items.forEach((i) => list.add(i));
  return list;
};

describe("Req 7: length", () => {
  test("an empty list has size 0", () => {
    expect(new List().size).toBe(0);
  });

  test("size grows when items are added at the end", () => {
    const list = new List();
    list.add(1);
    list.add(2);
    expect(list.size).toBe(2);
  });

  test("size grows when items are added at the front and in between", () => {
    const list = make(1, 3);
    list.addFirst(0);
    list.addAt(2, 2);
    expect(list.size).toBe(4);
  });

  test("duplicates are counted", () => {
    expect(make(5, 5, 5).size).toBe(3);
  });

  test("size does not change after set", () => {
    const list = make(1, 2, 3);
    list.set(1, 99);
    expect(list.size).toBe(3);
  });

  test("a failed insert does not change the size", () => {
    const list = make(1);
    expect(() => list.addAt(5, 9)).toThrow(RangeError);
    expect(list.size).toBe(1);
  });
});
