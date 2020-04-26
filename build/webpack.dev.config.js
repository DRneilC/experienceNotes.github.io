const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const merge = require('webpack-merge');
const webpackBaseConfig = require('./webpack.base.config.js');
const HtmlWebpackHarddiskPlugin = require('html-webpack-harddisk-plugin')
const fs = require('fs');
const config = require('../config');

const ip = 'http://192.168.0.24:8080';

process.env.NODE_ENV = config.dev.env;

fs.open('./config/env.js', 'w', function(err, fd) {
    const buf = 'export default "development";';
    fs.write(fd, buf, 0, buf.length, 0, function(err, written, buffer) {});
});

module.exports = merge(webpackBaseConfig, {
    devtool: '#source-map',
    devServer: {
        host: '0.0.0.0',
        port: 8051,
        proxy: { 
            '/api': {  //使用"/api"来代替"http://f.apiplus.c" 
                target: ip, //源地址 
                changeOrigin: true, //改变源 
                pathRewrite: { 
                  '^/api': ip //路径重写 
                } 
            }
        },
    },
    // output: {
    //     publicPath: '/dist/',
    //     filename: '[name].js',
    //     chunkFilename: '[name].chunk.js'
    // },
    plugins: [
        new ExtractTextPlugin({
            filename: '[name].css',
            allChunks: true
        }),
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendors',
            filename: 'vendors.js'
        }),
        new HtmlWebpackPlugin({
            filename: 'index.html',
            template: './src/template/index.ejs',
            inject: false
        }),
        new HtmlWebpackHarddiskPlugin({
            outputPath: config.build.htmlPath
        }),
    ]
});