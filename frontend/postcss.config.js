// postcss.config.js
import tailwindConfig from './tailwind.config.js'

export default {
  plugins: {
    tailwindcss: tailwindConfig,
    autoprefixer: {},
  },
}
