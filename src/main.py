import argparse
from cache import cache
from search import search

parser = argparse.ArgumentParser(description="CtrlF")
subparsers = parser.add_subparsers(dest="command",required=True)

parser_cache = subparsers.add_parser("cache")

parser_cache.add_argument("name",help="Name for new cache",type=str)
parser_cache.add_argument("cacheDirectory",help="Location where data should be cached", type=str)
parser_cache.add_argument("--server",help="SQL Server name",type = str,required=True)
parser_cache.add_argument("--database",help="Database name",type=str,required=True)
parser_cache.add_argument("--userid",help="username",type=str, required=True)
parser_cache.add_argument("--password",help="password", type=str, required=True)
parser_cache.set_defaults(func = lambda args: cache(args.name,args.cacheDirectory, args.server, args.database, args.userid, args.password))


parser_search = subparsers.add_parser("search")
parser_search.add_argument("cacheDirectory",help="cached location", type=str)
parser_search.add_argument("--searchString",help="string to search", type=str, required=True)
parser_search.add_argument("--exactMatch", help="Exact Match",type=bool, required=False, default=False)
parser_search.add_argument("--ignoreCase",type=bool, required=False, default=True)
parser_search.add_argument("--type", type=str,required=False, default="text", choices=["text","integer","decimal"])
parser_search.set_defaults(func = lambda args: search(args.cacheDirectory,args.searchString,args.exactMatch, args.ignoreCase, args.type))

if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)

