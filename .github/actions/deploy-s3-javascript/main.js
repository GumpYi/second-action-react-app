import { notice } from "@actions/core";
import github from "@actions/github";
import exec from "@actions/exec";

function run() {
  notice("Hello from my custom JavaScript Action!");
}

run();
