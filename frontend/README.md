# /www/

VHOST "www" is used for the homepage

https://www.vinhos.com

# /backoffice/

VHOST "backoffice" is used for the backoffice and website administration

https://backoffice.vinhos.com

# /app/

VHOST "app" is used for the mobile app

https://app.vinhos.com

# Command: pnpm vite

```commandline
vite/3.2.5

Usage:
  $ vite [root]

Commands:
  [root]           start dev server
  build [root]     build for production
  optimize [root]  pre-bundle dependencies
  preview [root]   locally preview production build

For more info, run any command with the `--help` flag:
  $ vite --help
  $ vite build --help
  $ vite optimize --help
  $ vite preview --help

Options:
  --host [host]           [string] specify hostname
  --port <port>           [number] specify port
  --https                 [boolean] use TLS + HTTP/2
  --open [path]           [boolean | string] open browser on startup
  --cors                  [boolean] enable CORS
  --strictPort            [boolean] exit if specified port is already in use
  --force                 [boolean] force the optimizer to ignore the cache and re-bundle
  -c, --config <file>     [string] use specified config file
  --base <path>           [string] public base path (default: /)
  -l, --logLevel <level>  [string] info | warn | error | silent
  --clearScreen           [boolean] allow/disable clear screen when logging
  -d, --debug [feat]      [string | boolean] show debug logs
  -f, --filter <filter>   [string] filter debug logs
  -m, --mode <mode>       [string] set env mode
  -h, --help              Display this message
  -v, --version           Display version number
```