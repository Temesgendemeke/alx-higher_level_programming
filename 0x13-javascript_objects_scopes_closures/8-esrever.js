#!/usr/bin/node
exports.esrever = function (list) {
let idx = list.length - 1
for (let i = 0; i <= idx; i++){
	for (let j = 0; j < idx/2; j++)
	{
		let temp = list[j]
		list[j] = list[idx - j]
		list[idx - j ] = temp
	}

}
return list
}
