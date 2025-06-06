﻿#!/usr/bin/env python3
import os
import sys
import uvicorn

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3025))
    host = os.environ.get('HOST', '0.0.0.0')
    
    print('Creative IA iniciando...')
    print(f'Porta: {port}')
    
    uvicorn.run(
        'src.main:app',
        host=host,
        port=port,
        reload=False,
        log_level='info'
    )
