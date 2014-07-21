//
//  ViewController.m
//  FollowApp
//
//  Created by Thibaut LE LEVIER on 21/07/2014.
//  Copyright (c) 2014 Thibaut LE LEVIER. All rights reserved.
//

#import "ViewController.h"
#import "SessionManager.h"

@interface ViewController ()

@property (strong, nonatomic) IBOutlet UILabel *helloLabel;

@end

@implementation ViewController

#pragma mark - birth and death
- (void)dealloc
{
    [[SessionManager sharedSession] removeObserver:self forKeyPath:@"login"];
}

#pragma mark - view lifecycle
- (void)viewDidLoad
{
    [super viewDidLoad];
    
    [[SessionManager sharedSession] addObserver:self forKeyPath:@"login" options:NSKeyValueObservingOptionNew context:nil];
    
    [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"http://follow-web-to-app.herokuapp.com/redirectToApp"]];
}


#pragma mark - KVO
-(void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
{
    if ([object isEqual:[SessionManager sharedSession]])
    {
        self.helloLabel.text = [NSString stringWithFormat:@"Hello\n%@",[SessionManager sharedSession].login];
    }
}


@end
