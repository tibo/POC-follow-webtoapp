//
//  NSURL+explodeURL.h
//  FollowApp
//
//  Created by Thibaut LE LEVIER on 21/07/2014.
//  Copyright (c) 2014 Thibaut LE LEVIER. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface NSURL (explodeURL)

-(NSArray *)urlComponentsForScheme:(NSString *)scheme;

@end
