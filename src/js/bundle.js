import { v4 as uuidv4 } from "uuid"; // 128bit crypto number generator.
import generateJoke from "./generateJoke"; // custom js..

import '../styles/nav.scss' // navigation scss.
import '../styles/main.scss' // main scss.

console.log(uuidv4())
console.log(generateJoke());
