//
//  APIClient.m
//  FollowApp
//
//  Created by Thibaut LE LEVIER on 22/07/2014.
//  Copyright (c) 2014 Thibaut LE LEVIER. All rights reserved.
//

#import "APIClient.h"

@implementation APIClient

+(void)getSessionForFollowKey:(NSString *)followKey withCallback:(void(^)(NSDictionary *session, NSError *error))callback
{
    NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"%@/getSession.json?follow_key=%@", SERVER_API_URL, followKey]];
    
    [NSURLConnection sendAsynchronousRequest:[NSURLRequest requestWithURL:url]
                                       queue:[NSOperationQueue mainQueue]
                           completionHandler:^(NSURLResponse *response, NSData *data, NSError *connectionError) {
                               
                               if (connectionError)
                               {
                                   callback(nil, connectionError);
                               }
                               else
                               {
                                   NSError *parsingError = nil;
                                   
                                   id result = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingAllowFragments error:&parsingError];
                                   
                                   if (parsingError)
                                   {
                                       callback(nil, parsingError);
                                   }
                                   else
                                   {
                                       callback(result, nil);
                                   }
                               }
                               
                           }];
}

@end
