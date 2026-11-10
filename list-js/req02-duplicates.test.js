const { List } = require("./list");

describe("Req 2: duplicates", () => {
  test("allows the same value many times", () => {
    const list = new List();
    list.add(5);
    list.add(5);
    list.add(5);
    expect(list.toArray()).toEqual([5, 5, 5]);
  });

  test("keeps both copies when a value is added again", () => {
    const list = new List();
    list.add(5);
    list.add(5);
    expect(list.toArray()).toHaveLength(2);
  });

  test("allows duplicate strings and objects too", () => {
    const list = new List();
    const obj = { a: 1 };
    list.add("a");
    list.add("a");
    list.add(obj);
    list.add(obj);
    expect(list.toArray()).toEqual(["a", "a", obj, obj]);
  });
});