#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
