function findBothMaxAndMin(arr) {

    // setup max, min base on odd or even array length;
    if (arr.length % 2 === 0) {
        var max = arr[0],
            min = arr[1];
    } else {
        var max = arr[0],
            min = max;
    }

    for (var i = 0; i < arr.length; i += 2) {

        var tmpMax = arr[i],
            tmpMin = arr[i + 1];

        if (arr[i] < arr[i + 1]) {
            tmpMax = arr[i + 1], tmpMin = arr[i];
        }

        max = tmpMax > max ? tmpMax : max;
        min = tmpMin < min ? tmpMin : min;

    }

    return "max = " + max + ", min = " + min;

}

