/*
    webpack plugin calls.
*/
const path = require('path')
// const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer')
// quick cooking this website html. ps) but this is just html not a django.html
// const HtmlWebpackPlugin = require('html-webpack-plugin')
// analyzing config this website.
// const bundleAnalyzerPlugin = require('webpack-bundle-analyzer').bundleAnalyzerPlugin
/*
    mode   : export mode. 
    entry  : convert file path.
    output : converted file path.
    devtool: converted javascript attributes are here. 
    module : what you want to export files and rules.
*/ 
module.exports = {
    // 1) 베이킹 타겟 및 베이킹 모드.
    // mode list production , development ,none
    mode   : 'production',
    entry  : {
        bundle : path.resolve(__dirname, 'src/js/bundle.js'),
    },
    // 2) 출력 셋업.
    output : {
        path : path.resolve(__dirname, 'static/js'), // convert 완료 후 저장소.
        // filename : '[name].[contenthash].js',        // convert 완료 후 저장될 이름.
        filename : '[name].js',        // convert 완료 후 저장될 이름.
        // clean : true,                                // run build 시 contenthash는 완료 파일 이외 모두 삭제.
        // assetModuleFilename : '[name].[ext]',     // convert 이미지의 이름과 확장자를 뽑아서 static/js 공간에 저장해준다. ps) 근데 이 기능은 좀 별로인거같다.
    },
    // 3) 자바스크립트 source map도 같이 출력.
    devtool : 'source-map',
    // devServer : {
    //     static : {
    //         directory : path.resolve(__dirname, 'static/js'),
    //     },
    //     port : 3000,
    //     open : true,
    //     hot : true,
    //     compress : true,
    //     historyApiFallback : true,
    // },
    module : {
        // use for scss set-up.
        rules : [
            {
                // scss 를 js에 병합.
                test : /\.scss$/,
                use : ['style-loader','css-loader','sass-loader'],
            },
            {
                // 자바스크립트 합치지만 node_modules는 제외한다.
                test : /\.js$/,
                exclude : /node_modules/,
                use : {
                    loader : 'babel-loader',
                    options : {
                        presets : ['@babel/preset-env'],
                    },
                },
            }
            // // 모든 이미지 확장자들을 받아서 저장한다.
            // {
            //     test : /\.(png|svg|jpg|jpeg|gif|ico)$/i,
            //     type : 'asset/resource'
            // },
        ]
    },
    plugins : [
        // create webpack basic html.
    //     new HtmlWebpackPlugin({
    //         title : 'Discord merlin-Bot',
    //         filename : 'main.html',
    //         template : 'templates/main.html',
    //     })
        // 웹사이트 분석할때만 쓸것.
        //    new BundleAnalyzerPlugin(),
    ]
}