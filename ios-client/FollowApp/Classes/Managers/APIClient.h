//
//  APIClient.h
//  FollowApp
//
//  Created by Thibaut LE LEVIER on 22/07/2014.
//  Copyright (c) 2014 Thibaut LE LEVIER. All rights reserved.
//

#import <Foundation/Foundation.h>

//#define SERVER_API_URL @"http://localhost:5000"
#define SERVER_API_URL @"http://follow-web-to-app.herokuapp.com"

@interface APIClient : NSObject

+(void)getSessionForFollowKey:(NSString *)followKey withCallback:(void(^)(NSDictionary *session, NSError *error))callback;

@end
