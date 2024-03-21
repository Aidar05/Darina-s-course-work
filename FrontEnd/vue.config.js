const { defineConfig } = require('@vue/cli-service')

// module.exports = defineConfig({
//   transpileDependencies: true
// })

module.exports = {
    devServer: {
        proxy: {
          '/api': {
            target: 'http://localhost:5000',  // Flask server URL
            changeOrigin: true
          }
        }
      },
    publicPath: process.env.NODE_ENV === 'production'
      ? '/static/'
      : '/'
  }