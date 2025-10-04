import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Aseprite Importer for Blender',
  description: 'Import Aseprite files as 3D pixel mesh in Blender',
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }]
  ],

  locales: {
    root: {
      label: 'English',
      lang: 'en',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'Guide', link: '/guide/' }
        ],
        sidebar: [
          {
            text: 'Guide',
            items: [
              { text: 'Installation', link: '/guide/installation' },
              { text: 'Usage', link: '/guide/usage' },
              { text: 'FAQ', link: '/guide/faq' }
            ]
          }
        ]
      }
    },
    ja: {
      label: '日本語',
      lang: 'ja',
      themeConfig: {
        nav: [
          { text: 'ホーム', link: '/ja/' },
          { text: 'ガイド', link: '/ja/guide/' }
        ],
        sidebar: [
          {
            text: 'ガイド',
            items: [
              { text: 'インストール', link: '/ja/guide/installation' },
              { text: '使い方', link: '/ja/guide/usage' },
              { text: 'FAQ', link: '/ja/guide/faq' }
            ]
          }
        ]
      }
    }
  },

  themeConfig: {
    logo: '/aseprite-importer-logo.gif',
    socialLinks: [
      { icon: 'github', link: 'https://github.com/kesera2/aseprite-importer-for-blender' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2025 kesera2'
    }
  }
})
