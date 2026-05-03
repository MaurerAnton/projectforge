import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import reactPlugin from 'eslint-plugin-react';
import importPlugin from 'eslint-plugin-import';
import globals from 'globals';

export default [
  js.configs.recommended,
  ...tseslint.configs.recommended,
  reactPlugin.configs.flat.recommended,
  importPlugin.flatConfigs.recommended,
  {
    files: ['src/**/*.{js,jsx,ts,tsx}'],
    languageOptions: {
      parserOptions: { ecmaFeatures: { jsx: true } },
      globals: { ...globals.browser },
    },
    settings: {
      react: { version: 'detect' },
      'import/resolver': { node: { extensions: ['.js', '.jsx', '.ts', '.tsx'] } },
    },
    rules: {
      '@typescript-eslint/no-explicit-any': 'off',
      'react/jsx-filename-extension': ['warn', { extensions: ['.jsx', '.js', '.tsx', '.ts'] }],
      'react/require-default-props': 'off',
      'react/jsx-props-no-spreading': 'off',
      indent: ['error', 4, { SwitchCase: 1 }],
      'react/jsx-indent': ['error', 4],
      'react/jsx-indent-props': ['error', 4],
      'import/extensions': ['error', 'ignorePackages', { js: 'never', jsx: 'never', ts: 'never', tsx: 'never' }],
      'object-curly-newline': ['error', {
        ObjectExpression: { minProperties: 4, multiline: true, consistent: true },
        ObjectPattern: { minProperties: 4, multiline: true, consistent: true },
        ImportDeclaration: { minProperties: 0, consistent: true },
        ExportDeclaration: { minProperties: 4, multiline: true, consistent: true },
      }],
    },
  },
  { ignores: ['node_modules', 'build', 'public'] },
];
