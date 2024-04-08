#!/usr/bin/node


function add(a, b){
    return a + b;
}

if (!process.argv[3] || isNaN(process.argv[2]) || isNaN(process.argv[3])){
    console.log("NaN")
}else {
    console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}    
