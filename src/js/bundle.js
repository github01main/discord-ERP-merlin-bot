import { v4 as uuidv4 } from "uuid"; // 128bit crypto number generator.
// import generateJoke from "./generateJoke"; // custom js..

//scss section.
import '../styles/main.scss' // main scss.
import '../styles/nav.scss' // navigation scss.
import '../styles/article.scss' // article scss.
import '../styles/community.scss' // community scss.

// .navigation-bar id를 128bit 암호화된다.
let insert_random_id_target = document.querySelector('.navigation-bar');
insert_random_id_target.id = uuidv4()

// .cat0lit 안에 있는 모든 id들은 128bit 암호화된다.
let insert_random_category_list_id = document.querySelectorAll('.cat0lit');
for(var i = 0; i < insert_random_category_list_id.length; i++) {
    insert_random_category_list_id[i].id = uuidv4()
}