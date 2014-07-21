//
//  SessionManager.m
//  FollowApp
//
//  Created by Thibaut LE LEVIER on 21/07/2014.
//  Copyright (c) 2014 Thibaut LE LEVIER. All rights reserved.
//

#import "SessionManager.h"

@implementation SessionManager

+ (instancetype)sharedSession
{
    static SessionManager *_sharedSession = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        _sharedSession = [[SessionManager alloc] init];
    });
    
    return _sharedSession;
}

@end
