const { List } = require("./list");

describe("Req 1: multiple data types", () => {
  test("stores mixed types unchanged", () => {
    const list = new List();
    const arr = [4];
    const obj = { a: 1 };

    [1, "two", true, null, arr, obj].forEach((v) => list.add(v));

    expect(list.toArray()).toEqual([1, "two", true, null, arr, obj]);
  });
});