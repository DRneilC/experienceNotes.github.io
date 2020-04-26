let util = {};

util.title = function(title) {
    title = title ? title : 'DrNeilC';
    window.document.title = title;
};

console.log(process.env)

util.sourceUrl = (process.env.NODE_ENV && process.env.NODE_ENV == "production") ? '' : '../src';

/**
 * 获取屏幕宽高
 */
util.getViewportSize = function () {
    return {
        width: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
        height: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
    };
};

export default util;