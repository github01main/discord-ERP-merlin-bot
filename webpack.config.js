/*
    npm run build후 저장할 js 위치를 불러오고 저장하기 위한 함수.
*/
const path = require('path') 
/*
    mode   : export mode. 
    entry  : convert file path.
    output : converted file path.
    module : 
*/ 
module.exports = {
    // mode list production , development ,none
    mode   : 'production',
    entry  : {
        bundle : path.resolve(__dirname, 'src/js/bundle.js'),
    },
    output : {
        path : path.resolve(__dirname, 'static/js'),
        filename : '[name].js'
    },
    module : {
        // use for scss set-up.
        rules : [
            {
                test : /\.scss$/,
                use : ['style-loader','css-loader','sass-loader']
            }
        ]
    }
}