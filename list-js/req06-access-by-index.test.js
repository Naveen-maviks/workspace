const { List } = require("./list");

const make = (...items) => {
  const list = new List();
  items.forEach((i) => list.add(i));
  return list;
};

describe("Req 6: access by index", () => {
  test("gets the first item", () => {
    expect(make("a", "b", "c").get(0)).toBe("a");
  });

  test("gets the last item", () => {
    expect(make("a", "b", "c").get(2)).toBe("c");
  });

  test("gets an item in the middle", () => {
    expect(make("a", "b", "c").get(1)).toBe("b");
  });

  test("gets items of different types", () => {
    const obj = { a: 1 };
    const list = make(1, "two", null, obj);
    expect(list.get(2)).toBeNull();
    expect(list.get(3)).toBe(obj);
  });

  test("reading does not change the list", () => {
    const list = make(1, 2, 3);
    list.get(1);
    expect(list.toArray()).toEqual([1, 2, 3]);
  });

  test("index past the end throws", () => {
    expect(() => make("a").get(1)).toThrow(RangeError);
  });

  test("negative index throws", () => {
    expect(() => make("a").get(-1)).toThrow(RangeError);
  });

  test("empty list throws", () => {
    expect(() => new List().get(0)).toThrow(RangeError);
  });
});
