  function isValid(stale, latest, otjson) {
    let result = stale.split("");
    let cursor = 0;
    otjson = JSON.parse(otjson);
    for (cmd of otjson) {
      if (cmd.op === "skip") {
        cursor = skip(cmd.count, result);
        if (cursor === false) return false;
      } else if (cmd.op === "insert") {
        result = insert(cmd.chars, result, cursor);
      } else if (cmd.op === "delete") {
        result = del(cmd.count, result, cursor);
        if (result === false) return false;
      }
    }

    return result.join("") === latest;
  }

  function skip(val, str) {
    if (val > str.length) return false;
    return val;
  }

  function insert(val, str, cur) {
    str.splice(cur, 0, val);
    return str;
  }

  function del(amt, str, cur) {
    if (amt > str.length - cur) return false;
    str.splice(cur, amt);
    return str;
  }
