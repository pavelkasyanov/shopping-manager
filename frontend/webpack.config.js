const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const Dotenv = require('dotenv-webpack');



module.exports = {
    mode: 'development',
    entry: './src/index.ts',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
        publicPath: '/',
    },
    // how and if to generate source maps
    devtool: 'eval-cheap-module-source-map',
    module: {
      rules: [
        { 
            test: /\.ts$/, 
            use: 'ts-loader', 
            exclude: /node_modules/ 
        },
        //Allows use of svelte
        {
            test: /\.svelte$/,
            use: {
                loader: 'svelte-loader',
            },
        },
        //Allows use of modern javascript
        {
            test: /\.js?$/,
            exclude: /node_modules/, //don't test node_modules folder
            use: {
                loader: 'babel-loader',
            },
        },
        {
          test: /\.s[ac]ss$/i,
          use: [
            // Creates `style` nodes from JS strings
            "style-loader",
            // Translates CSS into CommonJS
            "css-loader",
            // Compiles Sass to CSS
            "sass-loader",
          ],
        },
         //Allows use of images
         {
            test: /\.(jpg|jpeg|png|svg)$/,
            use: 'file-loader',
        }
      ],
    },
    //this is what enables users to leave off the extension when importing
    resolve: {
        extensions: ['.mjs', '.js', '.svelte'],
    },
    plugins: [
        //Allows to create an index.html in our build folder 
        new HtmlWebpackPlugin({
            template: path.resolve(__dirname, 'public/index.html'),
        }),
        //This gets all our css and put in a unique file
        new MiniCssExtractPlugin(),
        //take our environment variable in .env file
        //And it does a text replace in the resulting bundle for any instances of process.env.
        new Dotenv(),
    ],
    devServer: {
        historyApiFallback: true,
        hot: true,
        static: path.resolve(__dirname, 'dist'),
        port: 9000
    }
  };