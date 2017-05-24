<?php
// The program code to interpret
$program = readline();

// The memory
$memory = array();
for($i = 0; $i <= 2048; $i++) {
  $memory[$i] = 0;
}

$instructionPointer = 0;
$dataPointer = 0;

// Keeps track of all the loops in the program
$loopCount = 0;
$currentLoop = 0;
$loopPairs = array();
$unpairedLoops = array();

// Parse all the loops prior to running
for($i = 0; $i < (intval(strlen($program))); $i++) {
  switch($program[$i]) {
    case "[":
      $unpairedLoops[] = $i;
      break;
    case "]":
      // The loop's beginning has to be the most recent unpaired one
      $loopPairs[] = Array(array_pop($unpairedLoops), $i);
  }
}

// Create indexes of where everything begins/ends
$loopBeginnings = array();
$loopEnds = array();
foreach($loopPairs as $pair) {
  $loopBeginnings[$pair[1]] = $pair[0];
  $loopEnds[$pair[0]] = $pair[1];
}


// Run the program
while($instructionPointer < strlen($program)) {
  switch($program[$instructionPointer]) {
    case ">":
      $dataPointer++;
      break;
    case "<":
      $dataPointer--;
      break;
    case "+":
      $memory[$dataPointer]++;
      break;
    case "-":
      $memory[$dataPointer]--;
      break;
    case ".":
      echo chr($memory[$dataPointer]);
      break;
    case ",":
      $memory[$dataPointer] = ord(readline());
      break;
    case "[":
      // If the current memory cell is 0, skip to the end of the loop
      if($memory[$dataPointer] == 0) {
        $instructionPointer = $loopEnds[$instructionPointer];
      }
      break;
    case "]":
      // If the current memory cell is non-zero, return to the beginning of the loop
      if($memory[$dataPointer] != 0) {
        $instructionPointer = $loopBeginnings[$instructionPointer];
        // To counteract the incrementing at the end
        $instructionPointer--;
        break;
      }
  }

  $instructionPointer++;
}
?>
