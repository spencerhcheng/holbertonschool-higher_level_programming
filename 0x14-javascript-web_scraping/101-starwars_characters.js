#!/usr/bin/node

let myUrl = 'https://swapi.co/api/films/' + process.argv[2];
const request = require('request');
const nameList = {}
let nameArray = [];

request.get(myUrl, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  let json = JSON.parse(body)['characters'];
  for (let i = 0; i < json.length; i++) {
    request.get(json[i], function (err, res, body) {
      if (err) {
        return console.log(err);
      }
	let charNum = json[i].slice(-3).replace(/\//g, "");
	nameList[charNum] = JSON.parse(body)['name'];
	if (i === json.length - 1) {
		for (var key in nameList) {
			nameArray.push([parseInt(key), nameList[key]]);
		}
		console.log(nameArray.sort());
		quick_sort(nameArray, nameArray.length)
	//	for (let j = 0; j < nameArray.sort.length; j++) {
	//		console.log(nameArray[1]);
	//	}
	}
    });
  }
});

function quick_sort(array, size) {
	let low = 0;
	let high = size - 1;
	super_quick_sort(array, low, high, size);
}

function super_quick_sort(array, low, high, size) {
	if (low < high)
	{
		let partition_index = partition(array, low, high, size);
		super_quick_sort(array, low, partition_index - 1, size);
		super_quick_sort(array, partition_index + 1, high, size);
	}
}

function partition(array, low, high, size) {
	let pivot = array[high];
	let i = low - 1;
	let swap = 0;
	let temp = 0;

	for (let j = low; j <= high; j++) {
		if (array[j][0] <= pivot) {
			i++;
			temp = array[i];
			array[i] = array[j];
			array[j] = temp;
			swap = 1;
		}
	}

	temp = array[i + 1];
	array[i + 1] = array[high];
	array[high] = temp;
	let retval = i + 1;
	console.log(array);
	return (retval);
}
