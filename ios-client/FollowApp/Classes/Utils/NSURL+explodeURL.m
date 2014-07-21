//
//  NSURL+explodeURL.m
//  FollowApp
//
//  Created by Thibaut LE LEVIER on 21/07/2014.
//  Copyright (c) 2014 Thibaut LE LEVIER. All rights reserved.
//

#import "NSURL+explodeURL.h"

@implementation NSURL (explodeURL)

-(NSArray *)urlComponentsForScheme:(NSString *)scheme
{
    NSString * decodedString = [[[self absoluteString] stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding] substringWithRange:NSMakeRange(scheme.length, self.absoluteString.length - scheme.length)];
    
    return [decodedString componentsSeparatedByString:@"/"];
}

@end
